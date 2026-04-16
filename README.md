1.)Steps to run the application: 

    a.) Run the following command to install all the necessary packages:
        "pip install -r requirements.txt"
    
    b.) Create a .env file in the root directory and add your database credentials:
        DB_HOST=localhost
        DB_USER=your_username
        DB_PASSWORD=your_password
        DB_NAME=taskapi
        
    c.) Create the database in MySQL:
        "CREATE DATABASE taskapi;"
        
    d.) Run the application (tables will be created automatically on startup):
        "uvicorn main:app --reload --host 127.0.0.1 --port 8000"
        
    e.) Access the API documentation:
        Swagger UI: http://127.0.0.1:8000/docs
2.)Lets first walkthrough the database design.
We are subjected with two models,namely Category and Product.As mentioned in the task description,both of these models are related to each other,in the sense that each category may have many products,but each product has only one category.This clearly means that theres a one to many relation between category and product.

	a.)Now in order to implement the above,we create the following database models:
		1)Category:
			i)id -- integer -- serves as primary key.
			ii)name -- string -- describes the name of the category.
		2)Product:
			i)id -- integer -- serves as primary key.
			ii)name -- string -- describes the name of the product.
			iii)description -- string -- provides us with the description of the product.
			iv)price -- integer -- provides us with the price.
			v)category_id -- integer -- This is the foreign key that tells the category of the product.

	b.)There is a cascading operation as soon as a category is destroyed.That is,As soon as a category destroyed,all the products under it get deleted too.	

	c.)Corresponding to the database models,we also use pydantic models for requests sent by clients,since they help in validation.
				1.)Category:
					i)id -- integer 
					ii)name -- string
				2.)Product:
					i)id -- integer
					ii)name -- string
					iii)price -- integer
					iv)description -- string
			
				The above models are used for request to the server,helping validation.
				Apart from them,we use another pydantic model to send the response.
				The reason why choose another model for the sake of response is that we are meant to display the
				category details alongside the product details when the products are displayed.
				The ProductResponse model is as followed:
				
				3.)ProductResponse:
			
				
				ProductResponse
    					id -- integer 
    					name --  string
    					price -- integer 
    					description: string
    					category_id: integer

    					category: Category 
			
3.)API Walkthrough : The apis are mainly divided into two : The one for Categories and the other for Products.
	1.)Below is the api info with regards to categories:
	
		## Category APIs
				GET /api/categories?page={pageNumber}  
				Used to get categories with pagination (page number can be changed).
				
				POST /api/categories  
				Creates a new category.
				
				GET /api/categories/{id}  
				Fetch a category using its id.
				
				PUT /api/categories/{id}  
				Update category details using id.
				
				DELETE /api/categories/{id}  
				Deletes a category by id.
	
		## Product APIs
					GET /api/products?page={pageNumber}  
					Used to get products with pagination (can change page number).
					
					POST /api/products  
					Creates a new product.
					
					GET /api/products/{id}  
					Fetch a product using its id.
					
					PUT /api/products/{id}  
					Update product details using id.
					
					DELETE /api/products/{id}  
					Deletes a product by id.
