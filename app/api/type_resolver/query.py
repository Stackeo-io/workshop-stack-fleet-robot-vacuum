from typing import List

from ariadne import QueryType

from app.vacuum.clean_room import clean_room

query = QueryType()


@query.field("clean_room")
def resolve_clean_room(_, info, room: List[str], vacuum_position: List[int]) -> List[str]:
    actions = clean_room(room, vacuum_position)
    return actions
