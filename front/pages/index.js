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
      <div className="bg-r1 h-screen flex items-start justify-center pt-12 mt-10">
        <div className="bg-white lg:w-5/12 md:w-6/12 w-10/12 shadow-3xl">
        <div class="flex justify-center p-12 md:p-24">
            <div class="flex flex-col text-lg text-black font-bold">
            <h1 class="mb-5 text-center">USUÁRIO</h1>
            <div className="flex items-center justify-between mb-5">
                    <button
                      className="w-full bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => router.push("/aluno")}
                    >
                      ALUNO
                    </button>
              </div>
              <div className="flex items-center justify-between mb-5">
                    <button
                      className="w-full bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => router.push("/escola")}
                    >
                      ESCOLA
                    </button>
              </div>
              <div className="flex items-center justify-between mb-5">
                    <button
                      className="w-full bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => router.push("/adm")}
                    >
                      ADM
                    </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
