FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./ /emp-erp

WORKDIR /emp-erp
RUN ["chmod", "+x", "/emp-erp/entrypoint.sh"]
CMD ["uvicorn", "main:app", "--reload","--host","0.0.0.0"]

ENTRYPOINT ["/emp-erp/entrypoint.sh"]


#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

#COPY ./ /emp-erp

#WORKDIR /emp-erp  
#RUN chmod +x entrypoint.sh  
#CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]

#ENTRYPOINT ["C:\project\emp-erp/entrypoint.sh"]  # Correct path to entrypoint.doc