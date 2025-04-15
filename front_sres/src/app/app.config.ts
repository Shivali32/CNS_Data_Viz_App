import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';
import { CodeEditorComponent } from './code-editor/code-editor.component';

export const appConfig = {
  providers: [
    provideRouter([
      { path: '', component: CodeEditorComponent },
    ]),
    provideHttpClient()  
  ]
};
