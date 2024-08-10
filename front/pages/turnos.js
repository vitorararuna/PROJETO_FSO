import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export default function Turnos() {
//TODO - REDIRECT:
   //lógica para prazo encerrado
   //ógica para matrícula já realizada

  const router = useRouter();
  const { cpf } = router.query;

  const [vespertino, setVespertino] = useState("");
  const [matutino, setMatutino] = useState("");

  useEffect(() => {
    // TODO: Lógica para definir a disponibilidade dos turnos
    if (cpf == 3) {
      setVespertino("DISPONÍVEL");
      setMatutino("DISPONÍVEL");
    } else if (cpf == 4) {
      setVespertino("DISPONÍVEL");
      setMatutino("INDISPONÍVEL");
    } else if (cpf == 5) {
      setVespertino("INDISPONÍVEL");
      setMatutino("DISPONÍVEL");
    }
  }, [cpf]);

  const handleChooseTurno = (turno) => {
    if (turno === "MATUTINO") {
      router.push({
        pathname: "/matutino",
        query: { cpf: cpf }
      });
    } else if (turno === "VESPERTINO") {
      router.push({
        pathname: "/vespertino",
        query: { cpf: cpf }
      });
    }
  };

  return (
    <div className="flex flex-col">
      <div className="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr className="mb-5"></hr>
      </div>
      <div className="bg-r1 h-screen overflow-hidden flex items-center justify-center">
        <div className="bg-white lg:w-5/12 md:w-6/12 w-10/12 shadow-3xl border-4 border-gray-300 rounded-lg">
          <div className="flex justify-center p-12 md:p-24">
            <div className="flex flex-col text-lg text-black font-bold">
              <h1>TURNOS:</h1>
              <div className="text-lg text-black font-bold mt-5">
                <div className="flex items-center justify-between">
                  <h2 className="mr-2">MATUTINO</h2>
                  {matutino === "DISPONÍVEL" ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTurno("MATUTINO")}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mr-2 text-red-500">{matutino}</span>
                  )}
                </div>
                <div className="flex items-center justify-between mt-4">
                  <h2 className="mr-2">VESPERTINO</h2>
                  {vespertino === "DISPONÍVEL" ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTurno("VESPERTINO")}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mr-2 text-red-500">{vespertino}</span>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
