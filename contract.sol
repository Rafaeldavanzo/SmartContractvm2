pragma solidity ^0.8.0;

contract Greeter {

constructor() public {
   
}
string public greeting;
string public FullName;


  function setOwnerName(string memory _FullName) public {
    FullName =_FullName;
  }

  function greet() view public returns (string memory) {
    return greeting;
  }
}
