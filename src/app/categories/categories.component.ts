import { Component } from '@angular/core';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';

interface Category {
  id: number;
  name: string;
  image_url: string;
}

@Component({
  selector: 'app-categories',
  standalone: false,
  
  templateUrl: './categories.component.html',
  styleUrl: './categories.component.css'
})

export class CategoriesComponent {
  baseUrl = 'http://localhost:8000';
  categories: any[] = [];
  
  constructor(private productService: ProductService, private router: Router) {}
  
  ngOnInit() {
    this.productService.getCategories().subscribe((data) => {
      this.categories = data.map((category : Category)=> ({
        ...category,
        image_url: this.baseUrl + category.image_url 
      }));
    });
  }

  onCategoryClick(category: Category) {
    this.router.navigate([`products/category/${category.name}`])
  }
  
}
