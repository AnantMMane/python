package com.example.demo;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.reflections.Reflections;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import java.lang.reflect.Method;
import java.util.*;

public class MetadataExtractor {
    public static void main(String[] args) throws Exception {
        Reflections reflections = new Reflections("com.example.demo");

        // Collect all stereotype-annotated classes
        Set<Class<?>> serviceClasses = reflections.getTypesAnnotatedWith(Service.class);
        Set<Class<?>> componentClasses = reflections.getTypesAnnotatedWith(Component.class);
        Set<Class<?>> repositoryClasses = reflections.getTypesAnnotatedWith(Repository.class);
        Set<Class<?>> controllerClasses = reflections.getTypesAnnotatedWith(Controller.class);

        Set<Class<?>> allClasses = new HashSet<>();
        allClasses.addAll(serviceClasses);
        allClasses.addAll(componentClasses);
        allClasses.addAll(repositoryClasses);
        allClasses.addAll(controllerClasses);

        List<Map<String, Object>> classMetadata = new ArrayList<>();
        for (Class<?> clazz : allClasses) {
            Map<String, Object> classInfo = new HashMap<>();
            classInfo.put("className", clazz.getName());
            classInfo.put("annotations", Arrays.toString(clazz.getAnnotations()));

            List<Map<String, Object>> methods = new ArrayList<>();
            for (Method method : clazz.getDeclaredMethods()) {
                Map<String, Object> methodInfo = new HashMap<>();
                methodInfo.put("name", method.getName());
                methodInfo.put("returnType", method.getReturnType().getName());
                methodInfo.put("parameterTypes", Arrays.toString(method.getParameterTypes()));
                methodInfo.put("annotations", Arrays.toString(method.getAnnotations()));
                methods.add(methodInfo);
            }
            classInfo.put("methods", methods);
            classMetadata.add(classInfo);
        }

        // Write to JSON
        ObjectMapper mapper = new ObjectMapper();
        mapper.writerWithDefaultPrettyPrinter().writeValue(
            new java.io.File("internal_metadata.json"), classMetadata
        );
        System.out.println("Metadata exported to internal_metadata.json");
    }
} 