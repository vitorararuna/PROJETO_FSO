import { useState } from "react";
import { useRouter } from "next/router";

export default function Adm() {
  const [usuario, setUsuario] = useState("");
  const [senha, setSenha] = useState("");
  const [mensagemErro, setMensagemErro] = useState("");
  const router = useRouter();

  const handleLogin = (e) => {
    e.preventDefault();
    if (usuario === "adm" && senha === "adm") {
      router.push("/adm/relatorio");
    } else {
      setMensagemErro("Credencial inválida"); 
      setTimeout(() => setMensagemErro(""), 3000);
    }
  };

  return (
    <div className="flex flex-col">
      <div className="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr className="mb-5"></hr>
        <h3>Andre Dantas - 211010468</h3>
        <h3>Jean Karia - 211055290</h3>
        <h3>Vitor Araruna - 202060980</h3>
      </div>
      <div className="bg-r1 h-screen flex items-start justify-center pt-12 mt-10">
        <div className="bg-white lg:w-5/12 md:w-6/12 w-10/12 shadow-3xl">
          <h1 className="text-center text-black font-bold pt-10">ADMINISTRADOR</h1>
          <form className="p-12 md:p-24" onSubmit={handleLogin}>
            <div className="flex flex-col items-center text-lg text-black mb-6 md:mb-8">
              <div className="relative w-full mb-4">
                <svg
                  className="absolute left-3 top-1/2 transform -translate-y-1/2"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                >
                  <path d="M20.822 18.096c-3.439-.794-6.64-1.49-5.09-4.418 4.72-8.912 1.251-13.678-3.732-13.678-5.082 0-8.464 4.949-3.732 13.678 1.597 2.945-1.725 3.641-5.09 4.418-3.073.71-3.188 2.236-3.178 4.904l.004 1h23.99l.004-.969c.012-2.688-.092-4.222-3.176-4.935z" />
                </svg>
                <input
                  type="text"
                  id="usuario"
                  className="bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full"
                  placeholder="Usuário"
                  value={usuario}
                  onChange={(e) => setUsuario(e.target.value)}
                />
              </div>
              <div className="relative w-full mb-4">
                <svg
                  className="absolute left-2 top-1/2 transform -translate-y-1/2"
                  width="37"
                  height="37"
                  viewBox="0 0 24 24"
                >
                  <path
                    fillRule="evenodd"
                    d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                    clipRule="evenodd"
                  />
                </svg>
                <input
                  type="password"
                  id="password"
                  className="bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full"
                  placeholder="Senha"
                  value={senha}
                  onChange={(e) => setSenha(e.target.value)}
                />
              </div>
            </div>
            {mensagemErro && (
              <div className="mt-4 bg-red-500 text-white p-2 rounded text-center">
                {mensagemErro}
              </div>
            )}
            <button className="bg-gradient-to-b from-gray-700 to-gray-900 font-medium p-2 md:p-4 text-white uppercase w-full mt-4">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
