# Xunlei DPClient.Vod.1 ActiveX Control DownURL2 Method Remote Buffer Overflow Vulnerability
# CVE-2007-5064

import logging
log = logging.getLogger("Thug")

def DownURL2(self, arg0, *args):
    if len(arg0) > 1024:
        log.ThugLogging.add_behavior_warn('[Xunlei DPClient.Vod.1 ActiveX] DownURL2 Method Buffer Overflow',
                                   'CVE-2007-5064')


