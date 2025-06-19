<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="org.json.JSONObject,java.util.Date" %>
<%  // web request data 중 name값을 읽어오기
    request.setCharacterEncoding("utf-8"); 
    String name1 = request.getParameter("name");
    System.out.print("request data : name = " + name1);
    // JSON 객체 생성
    String[] items = {"item1", "item2"};
    java.util.Date today = new Date();
    JSONObject json = new JSONObject();
    json.put("name1", (name1 == null)? "ChatGPT" : name1);
    json.put("age", 3);
    json.put("items", items);
    // json.put("today", today);
    //json.put("language", "Korean");

    // 응답 설정 및 출력
    response.setContentType("application/json");
    response.setCharacterEncoding("UTF-8");
    response.getWriter().write(json.toString());
    // response.getWriter().close();
%>