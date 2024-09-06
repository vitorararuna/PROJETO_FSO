import { Inter } from "next/font/google";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { request_realizar_matricula, request_vespertino } from "../api/apiRoutes";

const inter = Inter({ subsets: ["latin"] });

export default function Vespertino() {
  const router = useRouter();
  const { cpf } = router.query;

  const [vespertino, setVespertino] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await request_vespertino();
        console.log("VESPERTINO:", response);
        setVespertino(response);
      } catch (error) {
        throw error;
      }
    };

    fetchData();
  }, [cpf]);

  const handleChooseTrilha = async (turma_id, trilha, turma) => {
    try {
      await request_realizar_matricula(parseInt(cpf), turma_id);
      console.log("Realizando matrícula...");
  
      router.push({
        pathname: "/aluno/matricula_realizada",
        query: { cpf: cpf, turno: "MATUTINO", trilha: "Trilha " + trilha + ": " + turma },
      });
    } catch (error) {
      console.error("Erro ao realizar matrícula", error);
      throw error;
    }
  };

  return (
    <div class="flex flex-col">
      <div class="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr class="mb-5"></hr>
      </div>
      <div className="bg-yellow-200 text-yellow-800 p-4 text-center font-bold">
        VOCÊ TEM APENAS 30 SEGUNDOS PARA REALZIAR A MATRÍCULA COMPLETA!
      </div>
      <div class="bg-r1 h-screen overflow-hidden flex items-center justify-center">
        <div class="bg-white shadow-3xl border-4 border-gray-300 rounded-lg">
          <div class="flex justify-center p-12 md:p-24">
            <div class="flex flex-col text-lg text-black font-bold">
            <h1 class="mb-5">TRILHAS:</h1>
              {vespertino.map((vespertino, index) => (
                <div key={index} className="flex items-center justify-between mt-8">
                  <h1 className="mr-2">{"Trilha " + vespertino.trilha + " " + vespertino.name}</h1>
                  {vespertino.vagas > 0 ? (
                    <button
                      className="bg-green-500 text-white font-bold py-1 px-4 rounded"
                      onClick={() => handleChooseTrilha(vespertino.id, vespertino.trilha, vespertino.name)}
                    >
                      ESCOLHER
                    </button>
                  ) : (
                    <span className="mx-2 text-red-500">INDISPONÍVEL</span>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
