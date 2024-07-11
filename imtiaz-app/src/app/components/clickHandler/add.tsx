"use client"
import { useState } from "react"
function Add() {
  const[count, setadd] = useState(0);
    const onclickHandler =()=>{
    setadd(count + 1) 
     
     }
  return (
     <>
    <h1 onClick={onclickHandler}> {count}</h1>
    </>
  )
}

export default Add