import React from 'react'
import { useParams, useLocation } from 'react-router-dom'
import { Container, Card, ListGroup } from 'react-bootstrap'

const Product = () => {
   const { productId } = useParams()
   const location = useLocation()

   // location.state가 객체일 경우 안전하게 처리
   const state = location.state ? JSON.stringify(location.state) : '없음'

   return (
      <Container className="mt-5">
         <Card>
            <Card.Header>
               <h3 className="mb-0">{productId}번 상품 상세 정보</h3>
            </Card.Header>
            <ListGroup variant="flush">
               <ListGroup.Item>🛍️ 제품: {location.hash || '없음'}</ListGroup.Item>
               <ListGroup.Item>📍 위치(pathname): {location.pathname}</ListGroup.Item>
               <ListGroup.Item>🔍 검색(query): {location.search || '없음'}</ListGroup.Item>
               <ListGroup.Item>📦 상태(state): {state}</ListGroup.Item>
            </ListGroup>
         </Card>
      </Container>
   )
}

export default Product
