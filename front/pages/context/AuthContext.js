import { createContext, useState, useContext } from "react";
import { useRouter } from "next/router";
import { request_logout } from "../api/apiRoutes";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [cpf, setCpfContext] = useState("");
  const [matriculou, setMatriculou] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [timer, setTimer] = useState(null);
  const router = useRouter();

  const login = () => {
    setIsLoggedIn(true);

    const timeout = setTimeout(() => {
      logout();
    }, 30000);

    setTimer(timeout);
  };

  const logout = async () => {
    setIsLoggedIn(false);
    if (matriculou == false) {
      await request_logout(cpf);
    }
    clearTimeout(timer); 
    router.push("/aluno"); 
  };

  const cancellTimer = () => {
      clearTimeout(timer); 
      setTimer(null);
  };

  return (
    <AuthContext.Provider value={{ setMatriculou, setCpfContext, isLoggedIn, login, logout, cancellTimer }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
