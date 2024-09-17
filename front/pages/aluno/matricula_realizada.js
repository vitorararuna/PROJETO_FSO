import { Inter } from "next/font/google";
import { useRouter } from "next/router";
import { request_logout } from "../api/apiRoutes";
import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";

const inter = Inter({ subsets: ["latin"] });

export default function Realizada() {
  const router = useRouter();
  const { cpf, turno, trilha } = router.query;
  const { cancellTimer } = useAuth(); 

  useEffect(() => {
    cancellTimer();
  }, []);

  const handleSair = async () => {
    await request_logout(cpf);
    router.push("/aluno");
  };

  return (
    <div class="flex flex-col">
      <div class="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr class="mb-5"></hr>
      </div>
      <div class="bg-r1 h-screen overflow-hidden flex items-center justify-center">
        <div class="bg-white lg:w-5/12 md:w-6/12 w-10/12 shadow-3xl border-4 border-gray-300 rounded-lg">
          <div class="flex justify-center p-12 md:p-24">
            <div class="flex flex-col text-lg text-black font-bold">
              <h1>MATRÍCULA REALIZADA PARA O CPF {cpf}</h1>
              <div class="text-lg text-black font-bold mt-4">
                <h3>
                  {trilha} - TURNO {turno}
                </h3>
              </div>
              <div
                onClick={handleSair}
                className="mt-8 bg-green-500 text-white p-2 rounded text-center cursor-pointer"
              >
                SAIR
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
