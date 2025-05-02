import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Container, Row, Col, Card } from 'react-bootstrap'

function Main() {
   const [timer, setTimer] = useState('00:00:00')

   // ⏱️ 타이머 useEffect로 한 번만 실행
   useEffect(() => {
      const updateTime = () => {
         const date = new Date()
         const hours = String(date.getHours()).padStart(2, '0')
         const minutes = String(date.getMinutes()).padStart(2, '0')
         const seconds = String(date.getSeconds()).padStart(2, '0')
         setTimer(`${hours}:${minutes}:${seconds}`)
      }

      updateTime()
      const interval = setInterval(updateTime, 1000)
      return () => clearInterval(interval)
   }, [])

   return (
      <Container className="mt-5">
         <h1 className="text-center mb-4">메인 페이지</h1>
         <h4 className="text-center text-muted mb-5">현재 시간: {timer}</h4>
         <Row className="justify-content-center">
            <Col xs={12} md={4}>
               <Card className="mb-3">
                  <Card.Body as={Link} to="/product/1" className="text-decoration-none text-dark">
                     <Card.Title>🍪 과자</Card.Title>
                     <Card.Text>달콤하고 바삭한 스낵</Card.Text>
                  </Card.Body>
               </Card>
            </Col>
            <Col xs={12} md={4}>
               <Card className="mb-3">
                  <Card.Body as={Link} to="/product/2" className="text-decoration-none text-dark">
                     <Card.Title>🥤 음료수</Card.Title>
                     <Card.Text>시원한 갈증 해소</Card.Text>
                  </Card.Body>
               </Card>
            </Col>
         </Row>
      </Container>
   )
}

export default Main
