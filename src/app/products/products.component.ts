import { Component } from '@angular/core';
import { ProductService } from '../product.service';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

interface Category {
  id: number;
  name: string;
  image_url: string;
}

@Component({
  selector: 'app-products',
  standalone: false,
  
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})

export class ProductsComponent {
  products: any[] = []
  categoryName: string | null = null;
  baseUrl = 'http://localhost:8000';

  constructor(private productService: ProductService, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.categoryName = params.get('categoryName')
      if(this.categoryName) {
        this.productService.getProductsByCategory(this.categoryName).subscribe((data)=> {
          this.products = data;
        })
      }
    })
  }
}
