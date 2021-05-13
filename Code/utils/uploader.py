from PersonalBlog import settings
from hashlib import md5
import time


def externalSitesIcons_uploadTo(instance, filename):
    string = "%s-%s" % (instance.title, str(time.time()))
    return "/".join(
        [
            settings.MediaPath.ExternalSiteIcons,
            "%s.png" % md5(string.encode('utf-8')).hexdigest()
        ]
    )


def coverImage_uploadTo(instance, filename):
    string = "%s-%s-%s" % (instance.title, str(time.time()), filename)
    return "/".join(
        [
            settings.CoverImages,
            "%s.png" % md5(string.encode('utf-8')).hexdigest()
        ]
    )
