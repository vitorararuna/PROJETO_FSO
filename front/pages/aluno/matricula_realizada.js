import { Inter } from "next/font/google";
import { useRouter } from "next/router";

const inter = Inter({ subsets: ["latin"] });

export default function Realizada() {
//TODO - REDIRECT:
   //lógica para prazo encerrado
   //ógica para matrícula já realizada

  
  const router = useRouter();
  const { cpf, turno, trilha } = router.query;

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
          <h3>{trilha} - TURNO {turno}</h3>
        </div>
      </div>
    </div>
  </div>
</div>
    </div>
  );
}
