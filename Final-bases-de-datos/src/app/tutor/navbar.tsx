// components/Navbar.tsx

import Link from 'next/link';
import * as DropdownMenu from '@radix-ui/react-dropdown-menu';
const Navbar = () => {
  return (
    <nav className="bg-blue-600 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/login" className="text-white font-bold text-lg">
          Flake
        </Link>
        <ul className="flex space-x-6">
          <li>
            <Link href="/tutor/horario" className="text-white hover:text-gray-300">
              Horario
            </Link>
          </li>
          <li>
            <Link href="/tutor/controldeasistencia" className="text-white hover:text-gray-300">
              Control de Asistencia
            </Link>
          </li>
          <li>
            <Link href="/tutor/calificaciones" className="text-white hover:text-gray-300">
              Calificaciones
            </Link>
          </li>
 {/* Dropdown de Aulas */}
 <li className="relative">
            <DropdownMenu.Root>
              <DropdownMenu.Trigger className="text-white hover:text-gray-300 cursor-pointer">
                Aulas
              </DropdownMenu.Trigger>

              <DropdownMenu.Content className="bg-white text-black shadow-lg rounded-md p-2 mt-2 w-48">
                <DropdownMenu.Item>
                  <Link href="/tutor/aulas/calificar" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Calificar
                  </Link>
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <Link href="/tutor/aulas/tomaasistencia" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Tomar Asistencia
                  </Link>
                </DropdownMenu.Item>
              </DropdownMenu.Content>
            </DropdownMenu.Root>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;

