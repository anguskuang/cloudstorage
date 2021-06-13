import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AysOzS5TFeegj-0cU8nuKvFxNVakZqu7Bfm3h_11vVGDdwnYojfyZGiG3jijOIkXPJEs4vVrAE8Hv3M5m3nNFRuhOe-GIchjBuvY00Jxa7Cp2Gu4CRnuLDQrx3OM2u6Lgq8_Qfc'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()