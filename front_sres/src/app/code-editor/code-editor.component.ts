// import { Component } from '@angular/core';
import { Component, ChangeDetectorRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Renderer2, ElementRef } from '@angular/core';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

    @Component({
      selector: 'app-code-editor',
      standalone: true,
      imports: [FormsModule, CommonModule, HttpClientModule],
      templateUrl: './code-editor.component.html',
      styleUrls: ['./code-editor.component.css']
    })
    export class CodeEditorComponent {
        language = 'python'; 
        code = '';
        outputUrl: string | null = null;
        outputHtmlUrl: string | null = null;  
    
        constructor(private http: HttpClient, private sanitizer: DomSanitizer) {}

        getSafeUrl(url: string): SafeUrl {
            return this.sanitizer.bypassSecurityTrustResourceUrl(url);
        }

        submitCode() {
            const payload = {
                language: this.language,
                code: this.code
            };
    
            
            this.http.post<any>('http://localhost:5000/run', payload, {
                headers: { 'Content-Type': 'application/json' }
            }).subscribe({
                next: (response) => {
                    this.outputUrl = 'http://localhost:5000' + response.plot_url;
                    this.outputHtmlUrl = 'http://localhost:5000' + response.plot_html_url;
                },
                error: (error) => {
                    console.error('Error:', error);
                }
            });
        }
            
        // isImage() {
        //     return this.outputUrl?.endsWith('.png');
        // }
            
        isHTML() {
            return this.outputHtmlUrl !== null;  
        }
    }
    

