pragma solidity ^0.8.0;

contract Greeter {

stringpublic greeting;
stringpublic FullName;


  function setOwnerName(stringmemory _FullName) public {

  FullName =_FullName;

  }


  function greet() view public returns (stringmemory) {

  return greeting;

  }

}
