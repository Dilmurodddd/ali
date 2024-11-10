from user import User
user = User("Dilmurod", "Mamarajabov", 22, "Student")
def test_user1():
    assert user.firstname == "Dilmurod"
    assert user.lastname == "Mamarajabov"
    assert user.age == 22
    assert user.job == "Student"
