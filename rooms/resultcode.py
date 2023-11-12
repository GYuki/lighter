class ResultCode(object):
    OK = 0
    PeerAlreadyJoined = 1
    PeerIdIsNull = 2
    ActiveJoiner = 3
    InactiveJoiner = 4
    RejoinerNotFound = 5
    RoomCreationError = 6
    GetRoomFromRoomCacheError = 7


DebugMessage = {
    ResultCode.OK: "OK",
    ResultCode.PeerAlreadyJoined: "Can't join to room while peer is already in room",
    ResultCode.PeerIdIsNull: "Peer is broken. No id is initialized",
    ResultCode.ActiveJoiner: "Can't join to room while actor is already in room and active",
    ResultCode.InactiveJoiner: "Can't rejoin to room while actor is already in room and active",
    ResultCode.RejoinerNotFound: "Can't rejoin to room. No joiner(actor) found in room"
}

