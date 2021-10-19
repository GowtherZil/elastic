# 👉 Elastic 👈

## 👼 El nacimiento

Elastic nació desde un proyecto muy diferente. La idea general que aún persiste era hacer un [ODM](https://www.doctrine-project.org/projects/doctrine-mongodb-odm/en/2.2/cookbook/mapping-classes-to-orm-and-odm.html)(*Object Document Mapping*) orientado a [MongoDB](https://www.mongodb.com) asyncrónico, más fácil, instuitivo y pytónico que los ya existentes(*[MotorEngine](https://motorengine.readthedocs.io/en/latest/), [UMongo](https://umongo.readthedocs.io/en/latest/) y [AsyncMongo](https://github.com/bitly/asyncmongo)*). Hacer el [ODM](https://www.doctrine-project.org/projects/doctrine-mongodb-odm/en/2.2/cookbook/mapping-classes-to-orm-and-odm.html) llevaba obligatoriamente a la necesidad de tener algún mecanismo que validara esquemas de datos. Aquí entra **Elastic**, un mecanismo para validar datos. 

Si me preguntaran como yo quería que fuera el resultado de programar con **Elastic** te diría:

> Cómodo como [pydantic](https://pydantic-docs.helpmanual.io/) y controlado como [marshamallow](https://marshmallow.readthedocs.io/en/stable/).


**Elastic** se implementó teniendo estos conceptos como base. Los nuevos esquemas o modelos se definen al igual que [pydantic](https://pydantic-docs.helpmanual.io/), usando las anotaciones de python para definir los campos pero al contrario de [pydantic](https://pydantic-docs.helpmanual.io/) los campos no son tipos básicos sino un único tipo extensible a traves de herencia, parecido a [marshamallow](https://marshmallow.readthedocs.io/en/stable/) y otros validadores/serializadores que usan el concepto de *campo como instancia de una clase*. De esta manera alcanzamos la mezcla de comodida y control que queríamos desde un principio.

## ☄ Uso básico

Para usar **Elastic** es necesario pasar por tres etapas:

- Definir los campos de los modelos necesarios para solucionar el problema.
- Contruir los campos necesarios.
- Construir los modelos.

## TODOS
- 🧪 Terminar las pruebas.
- 📚 Terminar el tutorial de **Uso Basico**.
- 🔥 Traducir al ingles.