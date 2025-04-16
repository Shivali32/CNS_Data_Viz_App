import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CodeEditorComponent } from './code-editor/code-editor.component';
import { SafePipe } from './safe.pipe';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  standalone: true,
  //   imports: [RouterOutlet],
//   imports: [CodeEditorComponent, SafePipe],
  imports: [CodeEditorComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
    title = 'front_sres';
    outputUrl: string = ''; 
    outputHtmlUrl: string = '';
  
    constructor(private sanitizer: DomSanitizer) {}
      
    getSafeUrl(url: string): SafeUrl {
      return this.sanitizer.bypassSecurityTrustResourceUrl(url);
    }
  }
