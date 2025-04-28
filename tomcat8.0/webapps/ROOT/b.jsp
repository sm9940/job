<%@ page contentType="application/json; charset=UTF-8" %>
<%@ page import="org.json.JSONObject" %>
<%
    request.setCharacterEncoding("utf-8");
    String name = request.getParameter("name");
    System.out.println("request data: name="+name);
    String[] items = { "item1", "item2" };
    JSONObject json = new JSONObject();
    json.put("name", (name == "")?"ChatGPT":name);
    json.put("age", 3);
    json.put("items", items);
    
    response.setContentType("application/json");
    response.setCharacterEncoding("UTF-8");
    response.getWriter().write(json.toString());
%>