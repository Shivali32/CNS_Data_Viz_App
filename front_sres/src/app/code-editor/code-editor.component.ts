// import { Component, ChangeDetectorRef } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { FormsModule } from '@angular/forms';
// import { CommonModule } from '@angular/common';  
// import { HttpClientModule } from '@angular/common/http';

// @Component({
//   selector: 'app-code-editor',
//   standalone: true,
//   imports: [FormsModule, CommonModule, HttpClientModule],
//   templateUrl: './code-editor.component.html',
//   styleUrls: ['./code-editor.component.css']
// })
// export class CodeEditorComponent {
//     language = 'python';  
//     code = ''; 
//     outputUrl: string | null = null;

//     constructor(private http: HttpClient, private cdRef: ChangeDetectorRef) {}

//     submitCode() {
//       const payload = {
//         language: this.language,
//         code: this.code
//       };

//       this.http.post<any>('http://localhost:5000/run', payload, {
//         headers: { 'Content-Type': 'application/json' }
//       }).subscribe({
//         next: (response) => {
//             const timestamp = new Date().getTime();
//             // this.outputUrl = 'http://localhost:5000' + response.url + '?t=' + timestamp;
//             this.outputUrl = 'http://localhost:5000' + response.url;
          
//           // Trigger change detection manually to update the DOM
//             this.cdRef.detectChanges();
//         },
//         error: (error) => {
//           console.error('Error:', error);
//         }
//       });
//     }

//     isImage() {
//       return this.outputUrl?.endsWith('.png') || this.outputUrl?.endsWith('.jpg');
//     }

//     isHTML() {
//       return this.outputUrl?.endsWith('.html');
//     }
// }




// import { Component } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { FormsModule } from '@angular/forms';
// import { CommonModule } from '@angular/common';    
// import { HttpClientModule } from '@angular/common/http';

//     @Component({
//       selector: 'app-code-editor',
//       standalone: true,
//       imports: [FormsModule, CommonModule, HttpClientModule],
//       templateUrl: './code-editor.component.html',
//       styleUrls: ['./code-editor.component.css']
//     })
//     export class CodeEditorComponent {
//         language = 'python';
//         code = '';
//         outputUrl: string | null = null;

//         constructor(private http: HttpClient) {}

//         submitCode() {
//           const payload = {
//             language: this.language,
//             code: this.code
//           };
          
//           this.http.post<any>('http://localhost:5000/run', payload, {
//             headers: { 'Content-Type': 'application/json' }
//           }).subscribe({
//             next: (response) => {
//             //   this.outputUrl = response.url;
//                 this.outputUrl = 'http://localhost:5000' + response.url;
//             },
//             error: (error) => {
//               console.error('Error:', error);
//             }
//           });
//         }

//         isImage() {
//           return this.outputUrl?.endsWith('.png') || this.outputUrl?.endsWith('.jpg');
//         }

//         isHTML() {
//           return this.outputUrl?.endsWith('.html');
//         }
//     }


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
        language = 'python';  // default language
        code = '';  // default starter code
        outputUrl: string | null = null;
        outputHtmlUrl: string | null = null;  // Store the HTML URL for Plotly/Bokeh/Altair
    
        constructor(private http: HttpClient, private sanitizer: DomSanitizer) {}

        getSafeUrl(url: string): SafeUrl {
            return this.sanitizer.bypassSecurityTrustResourceUrl(url);
        }

        submitCode() {
            const payload = {
                language: this.language,
                code: this.code
            };
    
            // Send the code to the backend for execution
            this.http.post<any>('http://localhost:5000/run', payload, {
                headers: { 'Content-Type': 'application/json' }
            }).subscribe({
                next: (response) => {
                    // Get both URLs (Matplotlib image and HTML plot)
                    this.outputUrl = 'http://localhost:5000' + response.plot_url;
                    this.outputHtmlUrl = 'http://localhost:5000' + response.plot_html_url;
                    // console.log('Image URL:', this.outputUrl);
                    console.log('HTML URL:', this.outputHtmlUrl);
                },
                error: (error) => {
                    console.error('Error:', error);
                }
            });
        }
    
        // Check if the output is an image (PNG)
        // isImage() {
        //     return this.outputUrl?.endsWith('.png');
        // }
    
        // Check if the output is HTML (for Plotly, Bokeh, Altair)
        isHTML() {
            return this.outputHtmlUrl !== null;  // We use plot_html_url for HTML output
        }
    }
    



    //     export class CodeEditorComponent {
//         language = 'python';  // default value
//         code = '';  // default starter code
//         outputUrl: string | null = null;

//         // constructor(private http: HttpClient) {}
//         // constructor(private http: HttpClient, private cdRef: ChangeDetectorRef) {}
//         constructor(private http: HttpClient, private renderer: Renderer2, private el: ElementRef) {}
//         plotUrls: { [key: string]: string } = {}; 

//         submitCode() {
//           const payload = {
//             language: this.language,
//             code: this.code
//           };

//           // Add Content-Type header explicitly (although Angular should do it by default)
//           this.http.post<any>('http://localhost:5000/run', payload, {
//             headers: { 'Content-Type': 'application/json' }
//           }).subscribe({
//             next: (response) => {
// //               this.outputUrl = response.url;
//                 this.outputUrl = 'http://localhost:5000' + response.url; 
//                 // const timestamp = new Date().getTime();
//                 // this.outputUrl = 'http://localhost:5000' + response.url + '?t=' + timestamp;

//                 // this.cdRef.detectChanges();
                
//             },
//             error: (error) => {
//               console.error('Error:', error);
//             }
//           });
//         }

//         isImage() {
//           return this.outputUrl?.endsWith('.png') || this.outputUrl?.endsWith('.jpg');
//         }

//         isHTML() {
//           return this.outputUrl?.endsWith('.html');
//         }

//     }
