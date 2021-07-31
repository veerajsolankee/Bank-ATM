import dropbox

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from,file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'hQptjmnvSUQAAAAAAAAAAXS6FBMBfFc6mvacG089mWdLTJ3-'
    transferdata = Transferdata(access_token)

    file_from = input("enter the file to be uploaded")
    file_to = input("enter the file name")

    transferdata.upload_file(file_from, file_to)
    print('file has been uploaded')
main()