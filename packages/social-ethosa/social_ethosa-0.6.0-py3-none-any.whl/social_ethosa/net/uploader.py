# -*- coding: utf-8 -*-
# author: ethosa

import time
import sys

from ..utils import Thread_VK, getValue, upl, upload_files


class Uploader:

    """
    docstring for uploader

    usage:
    vk.uploader.getUploadUrl('message_photo') # set url for uploading files.

    response = vk.uploader.uploadFile('photo.png')
    response1 = vk.uploader.uploadFile('photo1.png')
    response2 = vk.uploader.uploadFile('photo2.png')
    response3 = vk.uploader.uploadFile('photo3.png')
    print(response)
    """

    def __init__(self, vk=None, multi=None):
        self.vk = vk
        self.multi = multi
        self.errorMsg = lambda: sys.stdout.write("param \"vk\" undefined\n")
        self.working = False

        if self.vk:
            self.lang = self.vk.lang
            self.method = self.vk.method
            self.working = 1.0
            self.types = {
                "album_photo": ["file", lambda album_id, **kwargs: self.vk.photos.getUploadServer(album_id=album_id, **kwargs),
                                lambda response, album_id: self.method('photos.save', hash=response['hash'], album_id=album_id,
                                                                       server=response['server'],
                                                                       photos_list=response['photos_list'],
                                                                       aid=response['aid'])['response']],
                "wall_photo": ["file", lambda **kwargs: self.vk.photos.getWallUploadServer(**kwargs),
                               lambda response, **kwargs: self.method('photos.saveWallPhoto', hash=response['hash'],
                                                                      server=response['server'],
                                                                      photo=response['photo'],
                                                                      **kwargs)['response'][0]],
                "message_photo": ["photo", lambda **kwargs: self.vk.photos.getMessagesUploadServer(**kwargs),
                                  lambda response: self.method('photos.saveMessagesPhoto', hash=response['hash'],
                                                               server=response['server'],
                                                               photo=response['photo'])['response'][0]],
                "user_photo": ["photo", lambda **kwargs: self.vk.photos.getOwnerPhotoUploadServer(**kwargs),
                               lambda response: self.method('photos.saveOwnerPhoto', hash=response['hash'],
                                                            server=response['server'],
                                                            photo=response['photo'])['response']],
                "chat_photo": ["photo", lambda chat_id, **kwargs: self.vk.photos.getChatUploadServer(chat_id=chat_id, **kwargs),
                               lambda response: self.method('messages.setChatPhoto',
                                                            file=response['response'])['response']],
                "market_photo": ["photo", lambda group_id, **kwargs: self.vk.photos.getMarketUploadServer(group_id=group_id),
                                 lambda response, group_id: self.method('photos.saveMarketPhoto', group_id=group_id, photo=response['photo'],
                                                                        hash=response['hash'], server=response['server'],
                                                                        crop_data=response['crop_data'],
                                                                        crop_hash=response['crop_hash'])['response']],
                "market_album_photo": ["file", lambda group_id, **kwargs: self.vk.photos.getMarketAlbumUploadServer(group_id=group_id),
                                       lambda response, group_id: self.method('photos.saveMarketAlbumPhoto',
                                                                              group_id=group_id, photo=response['photo'],
                                                                              hash=response['hash'],
                                                                              server=response['server'])['response']],
                "audio": ["file", lambda **kwargs: self.vk.audio.getUploadServer(),
                          lambda response, title, artist: self.method('audio.save', title=title,
                                                                      artist=artist, audio=response['audio'],
                                                                      hash=response['hash'],
                                                                      server=response['server'])['response']],
                "audio_message": ["file",
                                  lambda peer_id, **kwargs: self.vk.docs.getMessagesUploadServer(type='audio_message', peer_id=peer_id, **kwargs),
                                  lambda response, **kwargs: self.method('docs.save', file=response['file'], **kwargs)['response']],
                "doc_message": ["file", lambda **kwargs: self.vk.docs.getMessagesUploadServer(**kwargs),
                                lambda response, **kwargs: self.method('docs.save', file=response["file"], **kwargs)['response']],
                "video": ["file", lambda **kwargs: self.vk.video.save(**kwargs)]
            }
        else:
            self.errorMsg()
        self.url = ''
        self.current = ''

    def getUploadUrl(self, type_obj, **kwargs):
        """get upload url for upload file
        Arguments:
            type_obj {str} -- see method getAllTypes()
            **kwargs {dict} -- extra arguments
        """
        if self.current != type_obj:
            if self.working:
                response = getValue(self.types, type_obj)[1](**kwargs)
                if "response" in response:
                    self.url = response["response"]["upload_url"]
                else:
                    sys.stdout.write("%s\n" % response)
                self.current = type_obj
                sys.stdout.write("get upload url for '%s'!\n" % type_obj)
            else:
                self.errorMsg()

    def uploadFile(self, file, **kwargs):
        """upload file on server

        Arguments:
            file {str} -- file path
            **kwargs {dict} -- extra arguments

        Returns:
            dict -- uploaded object

        Raises:
            ValueError -- link to server not getted
        """
        if self.url:
            file = upl(file, self.types[self.current][0])

            if len(self.types[self.current]) > 2:
                return self.types[self.current][2](upload_files(self.url, file), **kwargs)
            else:
                return upload_files(self.url, file)
        else:
            raise ValueError("You should get a link to upload to the server")

    def autoUpload(self, type_obj, files, typeRules={}, filesRules={}):
        """used for fast upload files at server

        Arguments:
            type_obj {str} -- see getAllTypes method
            files {list or str} -- files paths for uploading at server

        Keyword Arguments:
            typeRules {dict} -- rules for server (default: {{}})
            filesRules {dict} -- rules for uploading (default: {{}})

        Returns:
            list -- list of dicts uploaded files
        """
        if isinstance(files, str):
            files = [files]
        if self.current != type_obj:
            self.getUploadUrl(type_obj, **typeRules)
        out = []

        def add(i):
            out.append(self.uploadFile(i, **filesRules))
        for i in files:
            Thread_VK(add, i).start()
            time.sleep(0.2)
        while len(out) < len(files):
            pass  # wait
        return out

    def uploadMessagePhoto(self, files, formatting=0, **kwargs):
        """upload photo in message

        Arguments:
            files {list or str} -- files paths for uploading at server
            **kwargs {dict} -- extra arguments

        Keyword Arguments:
            formatting {bool} -- to apply formatting to the downloaded files (default: {0})

        Returns:
            list -- list of dicts (or list of str, if you make formatting to True)
        """
        response = self.autoUpload("message_photo", files, typeRules=kwargs)
        if formatting:
            return ["photo%s_%s" % (i["owner_id"], i["id"]) for i in response]
        else:
            return response

    def uploadVideo(self, files, formatting=0, **kwargs):
        """upload video

        Arguments:
            files {list or str} -- files paths for uploading at server
            **kwargs {dict} -- extra arguments

        Keyword Arguments:
            formatting {bool} -- to apply formatting to the downloaded files (default: {0})

        Returns:
            list -- list of dicts (or list of str, if you make formatting to True)
        """
        response = self.autoUpload("video", files, typeRules=kwargs)
        if formatting:
            return ["video%s_%s" % (i["owner_id"], i["video_id"]) for i in response]
        else:
            return response

    def getAllTypes(self):
        """get all upload types
        """
        return {key: self.types[key][1].__code__.co_varnames for key in self.types.keys()}
