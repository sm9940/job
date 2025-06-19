<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"  import="org.json.simple.JSONObject" %>
<%  response.setContentType("application/json");
    String input = request.getParameter("name");
    JSONObject obj = new JSONObject();
    obj.put("userName", input);
    obj.put("id", "1");
    obj.put("title", "delectus aut autem");
    obj.put("completed", "false");
%>
<% String data = obj.toJSONString(); %>
<% out.print(data);%>