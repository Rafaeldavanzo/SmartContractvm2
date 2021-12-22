pragma solidity ^0.8.0;

contract Greeter {

string public greeting;
string public FullName;


  function setOwnerName(stringmemory _FullName) public {
    FullName =_FullName;
  }

  function greet() view public returns (stringmemory) {
    return greeting;
  }
}
