# 👉 Elastic 👈

## 👼 Giving birth to it

Elastic was born from a very different proyect. The main idea that still persists was making an [ODM](https://www.doctrine-project.org/projects/doctrine-mongodb-odm/en/2.2/cookbook/mapping-classes-to-orm-and-odm.html)(*Object Document Mapping*) oriented to asyncrhonous [MongoDB](https://www.mongodb.com), easier and also more intuitive and pythonic than the already existing (*[MotorEngine](https://motorengine.readthedocs.io/en/latest/), [UMongo](https://umongo.readthedocs.io/en/latest/) and [AsyncMongo](https://github.com/bitly/asyncmongo)*). Making the [ODM](https://www.doctrine-project.org/projects/doctrine-mongodb-odm/en/2.2/cookbook/mapping-classes-to-orm-and-odm.html) took mandatory the need of having some sort of mechanism that could validate data schemas. Here is where **Elastic** entered, as a mechanism por validating data.

If they asked me how do i wanted the result of programming **Elastic** to be , i'll answer:

> Confortable as [pydantic](https://pydantic-docs.helpmanual.io/) and controlled as [marshamallow](https://marshmallow.readthedocs.io/en/stable/).

Si me preguntaran como yo quería que fuera el resultado de programar con **Elastic** te diría:

**Elastic** was implemented having these concepts as base. The new schemas or models define themselves as they'll do on [pydantic](https://pydantic-docs.helpmanual.io/), using the python notations for defining the fields but on the contrary of [pydantic](https://pydantic-docs.helpmanual.io/) the fields are not basic types but an only extensible type through inheritance, much like [marshamallow](https://marshmallow.readthedocs.io/en/stable/) and some other validators/serializators that use the same concept of *field as instance of a class*. This way we reach the mix of confortability and control that we wanted from the begining.



## ☄ Basic Usage

For using **Elastic** it's necesary to pass through this 3 stages:

- Defining the fields of the necessary models for problem's solution.
- Building the necessary fields.
- Building the models.

## TODOS
- 🧪 Finishing tests.
- 📚 Finishing **Basic Usage** tutorial.
- 🔥 English transaltion.
