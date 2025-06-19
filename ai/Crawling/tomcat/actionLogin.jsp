<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="org.json.JSONObject,java.util.Date" %>
<%  // web request data 중 name값을 읽어오기
    request.setCharacterEncoding("utf-8"); 
    String id = request.getParameter("id");
    String pwd = request.getParameter("pwd");
    System.out.print("request data : id, password = " + id + ", " + pwd);
    // JSON 객체 생성
    String[] items = {"item1", "item2"};
    java.util.Date today = new Date();
    JSONObject json = new JSONObject();
    json.put("id", (id == null)? "ChatGPT" : id);
    json.put("age", 30);
    json.put("password", pwd);
    // json.put("today", today);
    //json.put("language", "Korean");

    // 응답 설정 및 출력
    response.setContentType("application/json");
    response.setCharacterEncoding("UTF-8");
    response.getWriter().write(json.toString());
    // response.getWriter().close();
%>