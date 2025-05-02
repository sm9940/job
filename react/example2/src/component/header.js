import 'bootstrap/dist/css/bootstrap.min.css'
import { Navbar, Nav, Container } from 'react-bootstrap'
import React from 'react'
import { Link } from 'react-router-dom'

function Header() {
   return (
      <Navbar bg="dark" variant="dark" expand="lg">
         <Container>
            <Navbar.Brand as={Link} to="/">
               MyApp
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
               <Nav className="me-auto">
                  <Nav.Link as={Link} to="/">
                     홈
                  </Nav.Link>
                  <Nav.Link as={Link} to="/login">
                     로그인
                  </Nav.Link>
               </Nav>
            </Navbar.Collapse>
         </Container>
      </Navbar>
   )
}

export default Header
