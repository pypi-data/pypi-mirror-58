import json_store_client, uuid, base64

gentkn = lambda: ''.join(str(uuid.uuid4()).split('-'))+''.join(str(uuid.uuid4()).split('-'))

class SingleKeyStorage(object):
    def __init__(self, verbose=True):
        self.uploadlimit = 10000
        self.keylimit = 7500
        self.v = verbose
    def gettoken(self):
        return gentkn()
    def newclient(self, tkn=None):
        tkn = tkn or self.gettoken()
        c = json_store_client.Client(tkn)
        return c
    
    def split_chunks(self, raw, buff):
        total = len(raw)
        tosend = {}
        added = 0
        while added < total:
            ch = raw[added:added+buff]
            tosend[str(len(tosend))] = ch
            added += buff
        return tosend
    def store(self, raw):
        enc = base64.b64encode(raw if not type(raw) == str else raw.encode())
        split = self.split_chunks(enc, self.uploadlimit)
        tkn = self.gettoken()
        print("Using token: "+tkn) if self.v else None
        client = self.newclient(tkn=tkn)
        print('Uploading %i chunks' % len(split)) if self.v else None
        for i in split:
            client.store(i, {'data':split[i].decode()})
            print("Chunk %s sent" % i) if self.v else None
        return tkn, len(split)

    def retrieve(self, tkn, chunks):
        client = self.newclient(tkn=tkn)
        data = ''
        for i in range(0,chunks):
            data += client.retrieve(str(i))['data']
            print('Downloaded chunk %i' % i) if self.v else None
        return base64.b64decode(data)