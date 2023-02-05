import React, { useState } from "react";
import UserContext from "./UserContext";

const UserState = (props) => {

  const [user, setUser] = useState("user1");
  const [user2, setUser2] = useState("user2");


  return (
    <UserContext.Provider
      value={{
        user,
        user2

      }}
    >
      {props.children}
    </UserContext.Provider>
  );
};

export default UserState;
