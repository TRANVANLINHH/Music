def help_command():
    commands = {
        "!play": "Phát một bài hát hoặc thêm vào hàng đợi",
        "!skip": "Bỏ qua bài hát hiện tại",
        "!stop": "Dừng phát nhạc và xóa hàng đợi",
        "!queue": "Hiển thị danh sách phát hiện tại",
        "!clear": "Xóa hàng đợi",
        "!volume": "Thay đổi âm lượng",
        "!now": "Hiển thị thông tin bài hát đang phát",
        "!search": "Tìm kiếm bài hát",
        "!pause": "Tạm dừng bài hát",
        "!resume": "Tiếp tục phát",
        "!next": "Phát bài hát tiếp theo trong hàng đợi",
        "!loop": "Bật/tắt chế độ lặp lại",
        "!shuffle": "Xáo trộn hàng đợi",
        "!help": "Hiển thị tất cả các lệnh"
    }
    
    help_message = "Danh sách các lệnh:\n"
    for command, description in commands.items():
        help_message += f"{command}: {description}\n"
    
    return help_message.strip()
