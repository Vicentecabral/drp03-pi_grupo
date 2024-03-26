import styles from "./navbar.module.css"
import Link from "next/link"

export default function Navbar(){
    return(
        <nav>
            <ul>
                <li>
                    <Link href="/"><p>Home</p></Link>
                </li>
                <li>
                    <Link href="/login"><p>Login</p></Link>
                </li>
                <li>
                    <Link href="/lista"><p>Lista</p></Link>
                </li>
            </ul>
        </nav>
    )
}