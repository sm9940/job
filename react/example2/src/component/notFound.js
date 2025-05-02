import React from 'react'
import { Container, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom'

const NotFound = () => {
   return (
      <Container className="text-center mt-5">
         <h1 className="display-3">404</h1>
         <p className="lead">페이지를 찾을 수 없습니다.</p>
         <p>요청하신 페이지가 존재하지 않거나, 이동되었을 수 있습니다.</p>
         <Button variant="primary" as={Link} to="/">
            홈으로 돌아가기
         </Button>
      </Container>
   )
}

export default NotFound
