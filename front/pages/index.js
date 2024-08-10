import { useRouter } from "next/router";
import { useState } from "react";
import { CPFS } from "@/constants";

export default function Home() {
  const [cpf, setCpf] = useState("");
  const router = useRouter();

  const handleLogin = (e) => {
    e.preventDefault();
    if (CPFS.includes(cpf)) {

      
      if (cpf == 1) {
        //TODO: lógica para prazo encerrado
        router.push("/prazo_encerrado");
      } else if (cpf == 2) {
         //TODO: lógica para matrícula já realizada
        router.push({
          pathname: "/matricula_realizada",
          query: { cpf: 12345, turno: "MATUTINO", trilha: "TRILHA 1: ENEGRE-SER" },
        });
      } else {
        router.push({
          pathname: "/turnos",
          query: { cpf: cpf }
        });
      }
    } else {
      router.push("/invalido");
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
      <div className="bg-r1 h-screen overflow-hidden flex items-center justify-center">
        <div className="bg-white lg:w-5/12 md:w-6/12 w-10/12 shadow-3xl">
          <form className="p-12 md:p-24" onSubmit={handleLogin}>
            <div className="flex items-center text-lg text-black mb-6 md:mb-8">
              <svg className="absolute ml-3" width="24" viewBox="0 0 24 24">
                <path d="M20.822 18.096c-3.439-.794-6.64-1.49-5.09-4.418 4.72-8.912 1.251-13.678-3.732-13.678-5.082 0-8.464 4.949-3.732 13.678 1.597 2.945-1.725 3.641-5.09 4.418-3.073.71-3.188 2.236-3.178 4.904l.004 1h23.99l.004-.969c.012-2.688-.092-4.222-3.176-4.935z" />
              </svg>
              <input
                type="number"
                id="cpf"
                className="bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full"
                placeholder="CPF"
                value={cpf}
                onChange={(e) => setCpf(e.target.value)}
              />
            </div>
            <button className="bg-gradient-to-b from-gray-700 to-gray-900 font-medium p-2 md:p-4 text-white uppercase w-full">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
