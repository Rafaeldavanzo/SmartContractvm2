pragma solidity ^0.8.0;

contract Greeter {
  string public greeting;

  constructor() public {
    greeting = 'Hello';
    wint _id;
    string -firstname;
    string _lastName;
  }
  functions addPerson(String memory _firstName, string memory _LastName) public {
    peopleCount += 1;
    people[peopleCount] = Person(peopleCount, _firstName, -lastName);
  }
  function setGreeting(string memory _greeting) public {
    greeting = _greeting;
  }

  function greet() view public returns (string memory) {
    return greeting;
  
  }
}


