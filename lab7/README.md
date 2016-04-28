# Lab 7 - Web servers

## Exercises

### 1. Implementing a web server

#### a. Creating the server

Create a program acting as a web server running locally on your computer. The server should contain a list of humans, where each human is represented by a dictionary storing the name and the age of the human.

#### b. Handling one request

When your server receives a `GET` request for the resource `/humans`, it should send back a response containing information about all the humans stored on the server. You determine the content type (use HTML, XML, JSON, text, CSV...), but you need to set the headers in the response accordingly.

If you go to `localhost/humans` in a web browser, you should be able to see the response (information about all humans).

#### c. Handling another request

When your server receives a `GET` request for the resource `/humans/<id>`, where `<id>` is a none- negative integer, it should send back a response containing information about the human stored at index `<id>` in your human's list. You can assume there always exists a human at this index. Choose whichever content type you prefer, but remember to set the header in the response accordingly.

If you go to `localhost/humans/1` in a web browser, you should be able to see the response (information about the first human).

If you go to `localhost/humans/2` in a web browser, you should be able to see the response (information about the second human).

#### d. Computing mathematical expressions

Make your server able to handle `GET` requests with information in the query string looking like this:

```
/compute?left-operand=1&operation=add&right-operand=2
```

`left-operand` and `right-operand` can store any number, and `operation` can store `add`, `sub`, `mul`, or `div`. The response back from the server should contain the result you obtain when you apply the operands on the operation.

## Run

```sh
python3 server.py
```

## Test

### Get all humans

#### Command

```sh
curl "localhost:5000/humans"
```

#### Result

```json
{
    "1": {
        "age": 28,
        "name": "Mud Pack"
    },
    "2": {
        "age": 42,
        "name": "Able Crown"
    },
    "3": {
        "age": 20,
        "name": "Marina Thonder"
    }
}
```

### Get a human

#### Command

```sh
curl "localhost:5000/humans/1"
```

#### Result

```json
{
    "age": 28,
    "name": "Mud Pack"
}
```

### Compute mathematical expressions

#### Command

```sh
curl "localhost:5000/compute?left-operand=1&operation=add&right-operand=2"
```

#### Result

```json
{
    "query": "1 add 2",
    "result": "3"
}
```
