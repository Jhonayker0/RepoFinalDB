"use client";

import { useEffect, useState } from "react";
import type { Metadata } from "next";
import localFont from "next/font/local";
import "../globals.css";
import "@radix-ui/themes/styles.css";
import { Theme } from "@radix-ui/themes";
import Navbar from "./navbar";



const geistSans = localFont({
  src: "../fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "../fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});



export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [Rol, setRol] = useState<string | null>(null);

useEffect(() => {
  // Obtener el dato de la sesión al cargar la página
  const storedRol = sessionStorage.getItem("Rol");
  if (storedRol === null || storedRol !== "Administrador") {
    window.location.href = "/login";
  } 
}, []);
  return (

      <Theme>
        <Navbar />
        
      {children}

      </Theme>

  
  );
}
