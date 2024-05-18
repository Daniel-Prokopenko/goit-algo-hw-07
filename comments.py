class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def __str__(self):
        if self.is_deleted:
            return self.text
        return self.author + ": " + self.text

    def display(self, indent=""):
        print(indent + str(self))
        for reply in self.replies:
            reply.display(indent + "    ")


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

reply1_2 = Comment(
    "Думаю, це питання смаку. Хтось може знайти в ній глибокий зміст, а хтось – ні.",
    "Петро",
)
reply1.add_reply(reply1_2)

reply1_2_1 = Comment("Погоджуюся, Петре. Смаки різні, і це чудово.", "Вікторія")
reply1_2.add_reply(reply1_2_1)

reply2_1 = Comment(
    "Думаю, це чергова книга для думаючих глибоких роздумів. Цікаво, що саме за книга?",
    "Олена",
)
reply2.add_reply(reply2_1)

reply2_2 = Comment("Можливо, в ній є якісь нові погляди на старі проблеми?", "Ігор")
reply2.add_reply(reply2_2)

reply2.remove_reply()

reply2_3 = Comment("Нічого особливого, як на мене. Просто ще одна книга.", "Надія")
reply2.add_reply(reply2_3)

reply2_3_1 = Comment(
    "Ти, напевно, просто не знайшов у ній чогось, що тебе зацікавило.", "Юрій"
)
reply2_3.add_reply(reply2_3_1)

reply2_3_1.remove_reply()

reply2_3_2 = Comment(
    "Підтримую, Надіє. Кожен має свій власний погляд на різні книги.", "Олег"
)
reply2_3.add_reply(reply2_3_2)

root_comment.display()
