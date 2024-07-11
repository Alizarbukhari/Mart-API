import { APP_LINKS } from "../../utils/constants";
import Image from "next/image";
import { Input } from "../ui/input";
import Add from "../clickHandler/add";
import { FaSearch } from "react-icons/fa";
export function InputDemo() {
  return <Input type="email" placeholder="Email" />
}

import Link from "next/link";
import { ShoppingCart } from "lucide-react";
import { useState } from "react";

function Header() {
  return (
    <div className="p-5 flex justify-between items-center bg-sky-500">
     
      <div>
        <Image
          src={"/images/imtiaz1.png"}
          alt="logo-image"
          width={100}
          height={53}
        />
      </div>
      <div className="flex gap-10 items-center ">
        {APP_LINKS.map((link) => (
          <Link href={link.href}>
            <p className="font-semibold">{link.name}</p>
          </Link>
        ))}
      </div>
      <div className="relative inline-block">
        <Input placeholder="Search Products "  className="h-8"  /> 
        <FaSearch className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-600" />
      </div>
      <div className="w-10 h-10 rounded-full bg-slate-200 flex justify-center items-center relative">
        <div className="w-4 h-4 rounded-full flex justify-center items-center bg-red-500 absolute right-1 top-0">
        <button
          className="text-white text-xs"> <Add/> </button>
        </div>
        <ShoppingCart/>
      </div>
    </div>
  );
}

export default Header;