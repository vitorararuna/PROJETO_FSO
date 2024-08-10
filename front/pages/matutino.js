import Image from "next/image";
import { Inter } from "next/font/google";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

const inter = Inter({ subsets: ["latin"] });

export default function Matutino() {
//TODO - REDIRECT:
   //lógica para prazo encerrado
   //ógica para matrícula já realizada

  const router = useRouter();
  const { cpf } = router.query;

  const [trilha1, setTrilha1] = useState("");
  const [trilha2, setTrilha2] = useState("");
  const [trilha3, setTrilha3] = useState("");
  const [trilha4, setTrilha4] = useState("");

  useEffect(() => {
    // TODO: Lógica para definir a disponibilidade das trilhas
    if (cpf == 3) {
      setTrilha1("DISPONÍVEL");
      setTrilha2("DISPONÍVEL");
      setTrilha3("DISPONÍVEL");
      setTrilha4("DISPONÍVEL");
    } else if (cpf == 4) {
      setTrilha1("DISPONÍVEL");
      setTrilha2("INDISPONÍVEL");
      setTrilha3("INDISPONÍVEL");
      setTrilha4("DISPONÍVEL");
    } else if (cpf == 5) {
      setTrilha1("INDISPONÍVEL");
      setTrilha2("INDISPONÍVEL");
      setTrilha3("DISPONÍVEL");
      setTrilha4("INDISPONÍVEL");
    }
  }, [cpf]);

  const handleChooseTrilha = (trilha) => {
    console.log(`Escolhendo a ${trilha}`);
    router.push({
      pathname: "/matricula_realizada",
      query: { cpf: cpf, turno: "MATUTINO", trilha: trilha },
    });
  };

  return (
    <div class="flex flex-col">
      <div class="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr class="mb-5"></hr>
      </div>
      <div class="bg-r1 h-screen overflow-hidden flex items-center justify-center">
        <div class="bg-white shadow-3xl border-4 border-gray-300 rounded-lg">
          <div class="flex justify-center p-12 md:p-24">
            <div class="flex flex-col text-lg text-black font-bold">
              <h1 class="mb-5">TRILHAS:</h1>
              <div className="flex items-center justify-between">
                <h1>TRILHA 1: ENEGRE-SER</h1>
                {trilha1 === "DISPONÍVEL" ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTrilha("TRILHA 1: ENEGRE-SER")}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mx-2 text-red-500">{trilha1}</span>
                  )}
              </div>
              <div className="flex items-center justify-between">
                <h1>TRILHA 2: DINHEIRO NA MÃO É VENDAVAL</h1>
                {trilha2 === "DISPONÍVEL" ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTrilha("TRILHA 2: DINHEIRO NA MÃO É VENDAVA")}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mx-2 text-red-500">{trilha2}</span>
                  )}
              </div>
              <div className="flex items-center justify-between">
                <h1>TRILHA 3: ADMIRÁVEL MUNDO NOVO </h1>
                {trilha3 === "DISPONÍVEL" ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTrilha("TRILHA 3: ADMIRÁVEL MUNDO NOVO")}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mx-2 text-red-500">{trilha3}</span>
                  )}
              </div>
              <div className="flex items-center justify-between">
                <h1>TRILHA 4: AGROECOLOGIA </h1>
                {trilha4 === "DISPONÍVEL" ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTrilha("TRILHA 4: AGROECOLOGIA")}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mx-2 text-red-500">{trilha4}</span>
                  )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
