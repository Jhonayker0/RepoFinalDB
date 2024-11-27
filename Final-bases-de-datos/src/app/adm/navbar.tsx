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
            <Link href="/adm/gusuariopersona" className="text-white hover:text-gray-300">
              Personas
            </Link>
          </li>
          <li>
            <Link href="/adm/ginstitucion" className="text-white hover:text-gray-300">
              Instituciones
            </Link>
          </li>
          <li>
            <Link href="/adm/gaula" className="text-white hover:text-gray-300">
              Aulas
            </Link>
          </li>
          <li>
            <Link href="/adm/gestudiante" className="text-white hover:text-gray-300">
              Estudiantes
            </Link>
          </li>
          <li>
            <Link href="/adm/ghorario" className="text-white hover:text-gray-300">
              Horarios
            </Link>
          </li>
          <li>
            <Link href="/adm/gnotaestudiante" className="text-white hover:text-gray-300">
              Calificaciones
            </Link>
          </li>
          <li>
            <Link href="/adm/asistenciasestudiante" className="text-white hover:text-gray-300">
              A-estudiantes
            </Link>
          </li>
          <li>
            <Link href="/adm/asistenciastutor" className="text-white hover:text-gray-300">
              A-tutor
            </Link>
          </li>

          {/* Dropdown de Reportes */}
          <li className="relative">
            <DropdownMenu.Root>
              <DropdownMenu.Trigger className="text-white hover:text-gray-300 cursor-pointer">
                Reportes
              </DropdownMenu.Trigger>

              <DropdownMenu.Content className="bg-white text-black shadow-lg rounded-md p-2 mt-2 w-48">
                <DropdownMenu.Item>
                  <Link href="/adm/raulas" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Aulas
                  </Link>
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <Link href="/adm/restudiantes" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Estudiantes
                  </Link>
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <Link href="/adm/rinstituciones" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Instituciones
                  </Link>
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <Link href="/adm/rpersonas" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Personas
                  </Link>
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <Link href="/adm/rtutores" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Tutores
                  </Link>
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <Link href="/adm/rusuarios" className="block px-4 py-2 text-sm hover:bg-gray-100">
                    Usuarios
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
