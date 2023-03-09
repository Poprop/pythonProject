
def make_stickers(details_count: int, robot_part: str) -> list:
    message_robot = []
    detaill = 0
    while details_count > detaill:
        detaill += 1
        message = (f'{robot_part} detail #{detaill}')
        message_robot.append(message)
    return(message_robot)

