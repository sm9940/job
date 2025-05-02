import 'bootstrap/dist/css/bootstrap.min.css'
import React from 'react'
import { Container } from 'react-bootstrap'

function Footer() {
   return (
      <footer className="bg-dark text-white mt-5 py-3">
         <Container className="text-center">
            <p className="mb-1">&copy; 2025 MyCompany. All rights reserved.</p>
            <p className="mb-0">회사정보 · 저작권 · 연락처: contact@mycompany.com</p>
         </Container>
      </footer>
   )
}

export default Footer
