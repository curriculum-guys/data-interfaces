import os
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

class DriveManager:
    def __get_auth(self):
        auth = GoogleAuth()
        auth_file = "client_token.json"
        if os.path.exists(auth_file):
            auth.LoadCredentialsFile(auth_file)
        else:
            auth.LocalWebserverAuth()
            auth.SaveCredentialsFile(auth_file)
        self.auth = auth

    def get_drive(self):
        self.__get_auth()
        self.drive = GoogleDrive(self.auth)

    def get_folder(self, folder):
        files = self.drive.ListFile({'q': f"title = '{folder}'"}).GetList()
        return files

    def upload_file(self, filepath, filename, subpath=None):
        parents = self.get_folder(subpath) if subpath else []
        f = self.drive.CreateFile(dict(
            title=filename,
            parents=parents
        ))
        f.SetContentFile(filepath)
        f.Upload()
        f = None
