from random import randint

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 25)

    def add_member(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return {"status_code": 200, "message": "Miembo agregado con éxito"}

    def delete_member(self, member_id):
        self._members = [member for member in self._members if member["id"] != member_id]

    def update_member(self, member_id, new_member):
        for member in self._members:
            if member["id"] == member_id:
                member.update(new_member)

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member

    def get_all_members(self):
        return self._members

family_instance = Family(last_name="Jackson")

response = family_instance.add_member({
    "first_name": "Jack",
    "age": 28,
    "lucky_numbers": [5, 10, 15]
})

response = family_instance.add_member({
    "first_name": "John",
    "age": 32,
    "lucky_numbers": [7, 14, 21]
})

response = family_instance.add_member({
    "first_name": "Jill",
    "age": 34,
    "lucky_numbers": [3, 6, 9]
})

response = family_instance.add_member({
    "first_name": "Jane",
    "age": 30,
    "lucky_numbers": [2, 4, 8]
})


if response["status_code"] == 200:
    print("Miembro agregado con éxito")
else:
    print("Error al agregar el miembro:", response["message"])

print(f"Apellido de la familia: {family_instance.last_name}")

print("Todos los miembros:")
print(family_instance.get_all_members())

john_id = family_instance.get_member("John")
print(f"Miembro con ID 'John': {john_id}")

family_instance.update_member("John", {"age": 34})
print("Miembro 'John' actualizado:")
print(family_instance.get_all_members())

family_instance.delete_member("John")
print("Miembro 'John' eliminado:")
print(family_instance.get_all_members())
