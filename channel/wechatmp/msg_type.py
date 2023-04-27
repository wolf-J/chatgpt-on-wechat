from enum import unique, Enum


@unique
class MsgType(Enum):
    TEXT = "text"
    IMAGE = "image"
    VOICE = "voice"
    VIDEO = "video"
    SHORT_VIDEO = "shortvideo"
    LOCATION = "location"
    LINK = "link"
    EVENT = "event"
